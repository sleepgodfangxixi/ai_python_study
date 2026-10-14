# 环境踩坑记录（Windows）

这个仓库上真实踩过的坑，方便以后或者换电脑时快速排查。

## 1. PowerShell 写出来的文件是 UTF-16，Git 读不懂

**现象**

- `.gitignore` 里明明写了 `.venv/`、`.idea/`，结果 `.idea/` 还是被提交进了仓库。
- `README.md` 在 GitHub 网页上显示成一堆乱码。

**原因**

Windows PowerShell 5.1 里用 `>` 或 `Out-File` 重定向写文件，默认编码是
**UTF-16LE（带 BOM）**，文件开头两个字节是 `FF FE`。Git 只认 UTF-8，
于是把 `.gitignore` 当成乱码、所有规则全部失效；README 则是整个文件都乱。

**怎么确认**

```powershell
# 看文件头：FF FE 就是 UTF-16LE，EF BB BF 是 UTF-8 BOM，都没有才是干净 UTF-8
$b = [System.IO.File]::ReadAllBytes('.\README.md')
($b[0..7] | ForEach-Object { $_.ToString('X2') }) -join ' '

# 看某条忽略规则到底有没有命中（退出码 1 = 没命中）
git check-ignore -v .idea\xxx.iml
```

**正确写法**

```powershell
Set-Content .gitignore -Encoding utf8 -Value '.venv/','.idea/','__pycache__/'
```

或者直接用 VS Code / Notepad++ 保存为 UTF-8。PowerShell 7 的 `-Encoding utf8`
默认不带 BOM；Windows PowerShell 5.1 的 `utf8` 会带 BOM，写纯英文规则时
用 `-Encoding ascii` 最省心。

## 2. GitHub 加速器（Watt Toolkit）与 git 的证书冲突

**现象**

```
fatal: unable to access 'https://github.com/...':
SSL certificate problem: unable to get local issuer certificate
```

**原因**

Watt Toolkit（Steam++，根证书 `CN=SteamTools Certificate, O=BeyondDimension`）
把 `github.com` 用 hosts 指到 `127.0.0.1`，再自己签发证书做中间人加速。
而 Git for Windows 默认用 **OpenSSL 后端 + 自带的 ca-bundle.crt**，
里面没有这个 CA，证书校验必然失败。

**解决**

```powershell
git config --global http.sslBackend schannel
```

schannel 走 Windows 证书库，而 SteamTools 的根证书就装在
「受信任的根证书颁发机构」里，于是校验通过。

**注意事项**

- 这是全局设置，以后连**自签 CA 的内网 Git** 可能报证书错，
  临时切回来：`git -c http.sslBackend=openssl <命令>`。
- **不要**用 `git config --global http.sslVerify false` 绕过，
  那等于对所有网站关闭证书校验，凭据可能被中间人截获。
- 也**不要**删 hosts 里那批 `127.0.0.1 github*` 记录——那是加速通道，
  删掉之后直连 GitHub 大概率不通。

## 3. 首次把本地仓库推上 GitHub 的要点

1. **先配身份**，不配就会 `fatal: unable to auto-detect email address`：

   ```powershell
   git config --global user.name "你的名字"
   git config --global user.email "你的邮箱"
   ```

2. **必须先有提交再 push**。空仓库直接 push 会报
   `src refspec main does not match any`——不是分支名写错了，是没东西可推。

3. `origin` 已存在时 `git remote add` 会报 `already exists`，
   改用 `git remote set-url origin <新地址>`，
   用 `git remote -v` 确认改对了。

4. 私有仓库推送需要认证，出现
   `please complete authentication in your browser` 时去浏览器点一下确认，
   之后凭据会被自动记住，再推就不用登录了。

## 4. 上传前先想清楚哪些文件不该进仓库

- `.venv/`：虚拟环境，几百 MB，而且换电脑重建更好——必须忽略。
- `.idea/`：IDE 的个人配置，别人用不上——建议忽略。
- `__pycache__/`、`*.pyc`：Python 编译缓存——必须忽略。
- **密钥、token**：绝对不能提交。本仓库统一用环境变量。

如果某个文件在写 `.gitignore` **之前**就已经被 `git add` 过，
后加忽略规则是不生效的，要从索引里移除（磁盘文件不动）：

```powershell
git rm -r --cached .idea
git commit -m "chore: 停止跟踪 .idea"
```

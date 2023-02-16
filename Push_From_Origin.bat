@echo off

git remote add upstream https://github.com/ChenAi140/GLaDOS-CheckIn.git
git fetch upstream
echo 拉取更新完成！

echo 开始合并...
git checkout main
git merge upstream/main

echo 合并完成！

git push
echo push完成!

pause
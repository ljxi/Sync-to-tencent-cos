# Sync-to-tencent-cos

Github actions example:
.github/workflows/Sync-to-tencent-cos.yml
```
on:
  push:
    branches:
      - main
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout master
        uses: actions/checkout@v3
      - name: Sync-to-tencent-cos
        run: |
          pip install coscmd
          echo "Sync to tencent cos..."
          coscmd config -a ${{ secrets.SECRET_ID }} -s ${{ secrets.SECRET_KEY }} -b ${{ secrets.BUCKET }} -e cos.accelerate.myqcloud.com -m 30
          coscmd upload -rs ./ / --ignore "./.git/*","./.github/*","./README.md"
          coscmd abort
          echo "Delete old files..."
          curl https://raw.githubusercontent.com/ljxi/Sync-to-tencent-cos/main/Delete-old-files.py -o ./Delete-old-files.py
          python Delete-old-files.py
          echo "Sync to tencent cos done!"

```
Because GitHub actions' servers are located in the US, you'll need to turn on cos global acceleration to get normal upload speeds!

Secrets:
`BUCKET`
`SECRET_ID`
`SECRET_KEY`

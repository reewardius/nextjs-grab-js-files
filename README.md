# nextjs-grab-js-files

**How to find _buildManifest.js URL path**
1. Open Console
2. Paste next code
```
console.log('Full path "_buildManifest.js":', Array.from(document.querySelectorAll('script')).find(script => script.src.includes('_buildManifest.js'))?.src || 'File Not Found.');
```

**How to extract JS / JS.MAP files**
1. Run python script with file output
```
python next.py -u https://opensea.io/_next/static/40d453f28b1853bf39f6627ea80f4b3dbd611d7b/_buildManifest.js -o results.txt
```
2. Run python script with cli output
```
python next.py -u https://opensea.io/_next/static/40d453f28b1853bf39f6627ea80f4b3dbd611d7b/_buildManifest.js
```

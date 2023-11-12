# nextjs-pentest

**How to found _buildManifest.js**
1. Open Console
2. Paste next code
```
# console.log('Full path "_buildManifest.js":', Array.from(document.querySelectorAll('script')).find(script => script.src.includes('_buildManifest.js'))?.src || 'File Not Found.');
```

**How to extract JS / JS.MAP files**
1. Edit 10 line with your own **_buildManifest.js URL path**
2. Run python script
3. Find results in result_combined.txt file
```
> python next.py
```

# nextjs-grab-js-files

**How to find _buildManifest.js URL path**
1. Open Console
2. Paste next code
```
console.log('Full path "_buildManifest.js":', Array.from(document.querySelectorAll('script')).find(script => script.src.includes('_buildManifest.js'))?.src || 'File Not Found.');
```

**How to extract JS / JS.MAP files**
1. Edit 6 line with your own **_buildManifest.js URL path**
2. Run python script
```
> python next.py
```
3. Find results in result_combined.txt file

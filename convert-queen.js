const mammoth = require('mammoth');
const fs = require('fs');

async function convertQueenToMarkup() {
  try {
    console.log('Converting Queen of the South DOCX to HTML...');
    const buffer = fs.readFileSync('library/books/queen-of-the-south.docx');
    const res = await mammoth.convertToHtml({ buffer });
    
    // Create output directory
    const outDir = '.build/full-conversions';
    if (!fs.existsSync(outDir)) {
      fs.mkdirSync(outDir, { recursive: true });
    }
    
    // Write HTML version
    fs.writeFileSync(`${outDir}/queen-of-the-south-full.html`, res.value);
    console.log(`✅ HTML written to ${outDir}/queen-of-the-south-full.html`);
    console.log(`📊 Size: ${res.value.length} characters`);
    
    // Also try markdown conversion
    const mdRes = await mammoth.convertToMarkdown({ buffer });
    fs.writeFileSync(`${outDir}/queen-of-the-south-full.md`, mdRes.value);
    console.log(`✅ Markdown written to ${outDir}/queen-of-the-south-full.md`);
    console.log(`📊 Size: ${mdRes.value.length} characters`);
    
    console.log('\n🎯 Full conversion complete - ready for human review!');
    
  } catch (e) {
    console.error('❌ Conversion error:', e.message);
  }
}

convertQueenToMarkup();
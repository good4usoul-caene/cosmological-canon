// For PDF conversion, we need a PDF library. Let's try pdf-parse
const fs = require('fs');
const path = require('path');

async function convertBarabbasToMarkup() {
  try {
    // First, let's check if we have pdf-parse available
    let pdf;
    try {
      pdf = require('pdf-parse');
    } catch (e) {
      console.log('❌ pdf-parse not available. Installing...');
      const { execSync } = require('child_process');
      execSync('npm install pdf-parse', { stdio: 'inherit' });
      pdf = require('pdf-parse');
    }
    
    console.log('Converting Riddles of Barabbas PDF to text...');
    const buffer = fs.readFileSync('library/books/riddles-of-barabbas.pdf');
    const data = await pdf.default(buffer);
    
    // Create output directory
    const outDir = '.build/full-conversions';
    if (!fs.existsSync(outDir)) {
      fs.mkdirSync(outDir, { recursive: true });
    }
    
    // Write text version
    fs.writeFileSync(`${outDir}/riddles-of-barabbas-full.txt`, data.text);
    console.log(`✅ Text written to ${outDir}/riddles-of-barabbas-full.txt`);
    console.log(`📊 Size: ${data.text.length} characters`);
    console.log(`📄 Pages: ${data.numpages} pages`);
    
    // Create a basic markdown version with page breaks
    const pages = data.text.split('\f'); // Form feed character separates pages
    const markdown = pages.map((page, idx) => 
      `## Page ${idx + 1}\n\n${page.trim()}\n\n---\n`
    ).join('\n');
    
    fs.writeFileSync(`${outDir}/riddles-of-barabbas-full.md`, markdown);
    console.log(`✅ Markdown written to ${outDir}/riddles-of-barabbas-full.md`);
    
    console.log('\n🎯 Full PDF conversion complete - ready for human review!');
    
  } catch (e) {
    console.error('❌ PDF conversion error:', e.message);
  }
}

convertBarabbasToMarkup();
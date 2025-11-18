const fs = require('fs');

async function convertBarabbasPDF() {
  try {
    // Try importing pdf-parse properly
    const pdf = await import('pdf-parse');
    
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
    
    console.log('\n🎯 PDF conversion complete - ready for human review!');
    
  } catch (e) {
    console.error('❌ PDF conversion error:', e.message);
    console.log('\n💡 Alternative: You can manually save the PDF as text from a PDF viewer');
  }
}

convertBarabbasPDF();
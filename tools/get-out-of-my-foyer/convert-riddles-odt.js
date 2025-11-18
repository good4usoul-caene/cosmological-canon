const fs = require('fs');
const path = require('path');

async function convertRiddlesODT() {
  try {
    // ODT files are actually ZIP archives containing XML. Let's try to extract the content.xml
    console.log('Converting Ch x Ch Riddles.odt to text...');
    
    // For now, let's check if we have any ODT conversion libraries
    let AdmZip;
    try {
      AdmZip = require('adm-zip');
    } catch (e) {
      console.log('Installing adm-zip for ODT extraction...');
      const { execSync } = require('child_process');
      execSync('npm install adm-zip', { stdio: 'inherit' });
      AdmZip = require('adm-zip');
    }
    
    const zip = new AdmZip('library/books/Ch x Ch Riddles.odt');
    const zipEntries = zip.getEntries();
    
    // Look for content.xml which contains the main text
    const contentEntry = zipEntries.find(entry => entry.entryName === 'content.xml');
    
    if (contentEntry) {
      const contentXml = contentEntry.getData().toString('utf8');
      
      // Basic XML text extraction (remove tags)
      const textContent = contentXml
        .replace(/<[^>]*>/g, ' ')  // Remove XML tags
        .replace(/\s+/g, ' ')      // Normalize whitespace
        .trim();
      
      // Create output directory
      const outDir = '.build/full-conversions';
      if (!fs.existsSync(outDir)) {
        fs.mkdirSync(outDir, { recursive: true });
      }
      
      // Write text version
      fs.writeFileSync(`${outDir}/riddles-of-barabbas-odt-full.txt`, textContent);
      console.log(`✅ Text written to ${outDir}/riddles-of-barabbas-odt-full.txt`);
      console.log(`📊 Size: ${textContent.length} characters`);
      
      // Also save the raw XML for more detailed analysis if needed
      fs.writeFileSync(`${outDir}/riddles-of-barabbas-content.xml`, contentXml);
      console.log(`✅ Raw XML written to ${outDir}/riddles-of-barabbas-content.xml`);
      
      console.log('\n🎯 ODT conversion complete - ready for human review!');
      
    } else {
      console.error('❌ Could not find content.xml in ODT file');
      console.log('Available entries:', zipEntries.map(e => e.entryName));
    }
    
  } catch (e) {
    console.error('❌ ODT conversion error:', e.message);
  }
}

convertRiddlesODT();
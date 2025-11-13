const mammoth = require('mammoth');
const fs = require('fs');
const { JSDOM } = require('jsdom');

async function debugScanner() {
  try {
    const buffer = fs.readFileSync('library/books/queen-of-the-south.docx');
    const res = await mammoth.convertToHtml({ buffer });
    const html = res.value;
    const dom = new JSDOM(html);
    const doc = dom.window.document;
    
    console.log('=== BOLD ELEMENTS (Matthew) ===');
    const bolds = doc.querySelectorAll('strong, b');
    console.log('Found bold elements:', bolds.length);
    if (bolds.length > 0) {
      console.log('First bold:', bolds[0].textContent.trim().substring(0, 100));
    }
    
    console.log('\n=== ITALIC ELEMENTS (Luke) ===');
    const italics = doc.querySelectorAll('em, i');
    console.log('Found italic elements:', italics.length);
    if (italics.length > 0) {
      console.log('First italic:', italics[0].textContent.trim().substring(0, 100));
    }
    
    console.log('\n=== RED ELEMENTS (John) ===');
    const allEls = doc.querySelectorAll('*');
    let redCount = 0;
    allEls.forEach(el => {
      const style = el.getAttribute && (el.getAttribute('style') || '');
      if (style && /red/i.test(style)) {
        redCount++;
        if (redCount === 1) {
          console.log('First red element:', el.textContent.trim().substring(0, 100));
          console.log('Red style:', style);
        }
      }
    });
    console.log('Found red elements:', redCount);
    
  } catch (e) {
    console.error('Error:', e.message);
  }
}

debugScanner();
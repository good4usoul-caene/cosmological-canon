const mammoth = require('mammoth');
const fs = require('fs');
const { JSDOM } = require('jsdom');

async function findLimitedGospelContent() {
  try {
    const buffer = fs.readFileSync('library/books/queen-of-the-south.docx');
    const res = await mammoth.convertToHtml({ buffer });
    const html = res.value;
    const dom = new JSDOM(html);
    const doc = dom.window.document;
    
    console.log('=== THE 2 UNDERLINED PASSAGES (Mark) ===');
    const underlines = doc.querySelectorAll('u');
    underlines.forEach((el, idx) => {
      console.log(`\nUnderline ${idx + 1}:`);
      console.log(`Text: "${el.textContent.trim()}"`);
      console.log(`Context: "${el.parentElement?.textContent.trim().substring(0, 200)}..."`);
    });
    
    console.log('\n=== THE 1 RED PASSAGE (John) ===');
    const allEls = doc.querySelectorAll('*');
    allEls.forEach(el => {
      const style = el.getAttribute && (el.getAttribute('style') || '');
      if (style && /red/i.test(style)) {
        console.log(`Text: "${el.textContent.trim()}"`);
        console.log(`Style: ${style}`);
        console.log(`Context: "${el.parentElement?.textContent.trim().substring(0, 200)}..."`);
      }
    });
    
  } catch (e) {
    console.error('Error:', e.message);
  }
}

findLimitedGospelContent();
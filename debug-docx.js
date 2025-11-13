const mammoth = require('mammoth');
const fs = require('fs');

async function testDocx() {
  try {
    const buffer = fs.readFileSync('library/books/queen-of-the-south.docx');
    const res = await mammoth.convertToHtml({ buffer });
    console.log('HTML length:', res.value.length);
    console.log('First 500 characters:');
    console.log(res.value.substring(0, 500));
    console.log('\n--- Looking for formatting ---');
    console.log('Bold tags:', res.value.match(/<strong>|<b>/g)?.length || 0);
    console.log('Italic tags:', res.value.match(/<em>|<i>/g)?.length || 0);
    console.log('Underline tags:', res.value.match(/<u>|<ins>/g)?.length || 0);
    console.log('Red text:', res.value.match(/red/gi)?.length || 0);
  } catch (e) {
    console.error('Error:', e.message);
  }
}

testDocx();
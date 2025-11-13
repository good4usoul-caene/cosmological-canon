const mammoth = require('mammoth');
const fs = require('fs');

async function checkUnderlineAndRedHTML() {
  try {
    const buffer = fs.readFileSync('library/books/queen-of-the-south.docx');
    const res = await mammoth.convertToHtml({ buffer });
    const html = res.value;
    
    console.log('=== SEARCHING FOR UNDERLINE PATTERNS ===');
    console.log('text-decoration: underline:', (html.match(/text-decoration[^>]*underline/gi) || []).length);
    console.log('text-decoration-line: underline:', (html.match(/text-decoration-line[^>]*underline/gi) || []).length);
    console.log('<u> tags:', (html.match(/<u[^>]*>/gi) || []).length);
    console.log('<ins> tags:', (html.match(/<ins[^>]*>/gi) || []).length);
    
    console.log('\n=== SEARCHING FOR RED PATTERNS ===');
    console.log('color: red:', (html.match(/color[^>]*red/gi) || []).length);
    console.log('color: #ff0000:', (html.match(/color[^>]*#ff0000/gi) || []).length);
    console.log('color: rgb(255,0,0):', (html.match(/color[^>]*rgb\(255,0,0\)/gi) || []).length);
    
    console.log('\n=== SAMPLE HTML WITH POSSIBLE UNDERLINE ===');
    const underlineMatch = html.match(/[^>]{0,100}text-decoration[^<]{0,100}/i);
    if (underlineMatch) {
      console.log(underlineMatch[0]);
    }
    
    console.log('\n=== SAMPLE HTML WITH POSSIBLE RED ===');
    const redMatch = html.match(/[^>]{0,100}color[^<]{0,200}/i);
    if (redMatch) {
      console.log(redMatch[0]);
    }
    
  } catch (e) {
    console.error('Error:', e.message);
  }
}

checkUnderlineAndRedHTML();
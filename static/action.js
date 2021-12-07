const calc = document.getElementById('calc');
const clean = document.getElementById('clean');

calc.onclick = async () => {
  const terms = document.getElementsByClassName('terms');

  let isEmpty = false;
  const values = []

  for (term of terms) {
    if (!term.value) isEmpty = true;
    else values.push(term.value);
  }

  if (isEmpty) alert("Please enter necesary values")
  else {
    datas = await calculate(values)

    for (data of datas) {
      insertToDom(data)
    }

    clean.style.display = 'block'
    calc.style.display = 'none'
  }
}

clean.onclick = async () => {
  const result = document.querySelector('.results');
  const terms = document.getElementsByClassName('terms');

  for (term of terms) {
    term.value = ''
  }

  result.innerHTML = '';

  calc.style.display = 'block';
  clean.style.display = 'none';
}

function insertToDom(data) {
  const result = document.querySelector('.results');
  const vars = data['variables'];
  let strVars = '';
  let num = '&nbsp;';

  for (v of vars) {
    strVars += ` ${v['var']}
      <sup>${v['pow'] == 1 ? '' : v['pow']}</sup>
    `;
  }

  if (data['num'] < 0)
    num += '−&nbsp;' + coefficient(data['num'] * -1, data['den']);
  else if (result.childElementCount) {
    num += '+&nbsp;'

    if (data['num'] > 1)
      num += coefficient(data['num'], data['den']);
  } else if (data['num'] > 1 || !vars.length)
    num += coefficient(data['num'], data['den']);

  const strTerm = `
    <span>
      ${num}
      ${strVars}
    </span>
  `

  result.insertAdjacentHTML('beforeend', strTerm)
}

function coefficient(num, den) {
  result = ''

  if (den != 1)
    result += `
      <span class="fraction">
        <span>${num}</span>
        <span>${den}</span>
      </span>
    `;
  else
    result = num;

  return result;
}

async function calculate(values) {
  bodies = {
    firstTerm: values[0],
    secTerm: values[1],
    pow: parseInt(values[2])
  }

  const jsonfy = await fetch('/binomio', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(bodies)

  });

  const data = await jsonfy.json();

  return data;
}
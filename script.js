// ============================================================
//  Guía de Estudio – Grado Sexto | Monterrosales Homeschool
//  script.js – Navegación + Motor de calificación de simulacros
// ============================================================

// ========== NAVIGATION ==========
  function showSection(id, tab) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    tab.classList.add('active');
  }

  // ========== QUIZ NAVIGATION ==========
  function showQuiz(id, btn) {
    document.querySelectorAll('.quiz-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active-q'));
    document.getElementById('quiz-' + id).classList.add('active');
    btn.classList.add('active-q');
  }

  // ========== GRADING ==========
  const correctAnswers = {
    quimica: {
      q1:'b',q2:'c',q3:'a',q4:'b',q5:'ac',q6:'d',q7:'b',q8:'a',q9:'c',q10:'b',
      q11:'d',q12:'c',q13:'b',q14:'a',q15:'d',q16:'b',q17:'c',q18:'a',q19:'b',q20:'d'
    },
    biologia: {
      b1:'c',b2:'b',b3:'a',b4:'c',b5:'d',b6:'b',b7:'a',b8:'b',b9:'d',b10:'b',
      b11:'b',b12:'c',b13:'a',b14:'b',b15:'a',b16:'c',b17:'b',b18:'ac',b19:'b',b20:'abd'
    },
    lenguaje: {
      l1:'b',l2:'a',l3:'c',l4:'a',l5:'b',l6:'d',l7:'b',l8:'c',l9:'a',l10:'b',
      l11:'c',l12:'a',l13:'a',l14:'d',l15:'b',l16:'c',l17:'b',l18:'a',l19:'a',l20:'b'
    },
    sociales: {
      s1:'c',s2:'b',s3:'a',s4:'c',s5:'d',s6:'b',s7:'a',s8:'c',s9:'b',s10:'a',
      s11:'c',s12:'b',s13:'d',s14:'c',s15:'b',s16:'b',s17:'abc',s18:'c',s19:'b',s20:'a'
    },
    matematicas: {
      m1:'b',m2:'c',m3:'a',m4:'b',m5:'c',m6:'b',m7:'a',m8:'c',m9:'b',m10:'d',
      m11:'b',m12:'c',m13:'b',m14:'a',m15:'d',m16:'b',m17:'a',m18:'c',m19:'d',m20:'b'
    }
  };

  const questionLabels = {
    quimica: ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20'],
    biologia: ['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12','b13','b14','b15','b16','b17','b18','b19','b20'],
    lenguaje: ['l1','l2','l3','l4','l5','l6','l7','l8','l9','l10','l11','l12','l13','l14','l15','l16','l17','l18','l19','l20'],
    sociales: ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20'],
    matematicas: ['m1','m2','m3','m4','m5','m6','m7','m8','m9','m10','m11','m12','m13','m14','m15','m16','m17','m18','m19','m20']
  };

  function getAnswer(name, isMulti) {
    if (isMulti) {
      const checked = document.querySelectorAll(`input[name="${name}"]:checked`);
      return Array.from(checked).map(c => c.value).sort().join('');
    } else {
      const sel = document.querySelector(`input[name="${name}"]:checked`);
      return sel ? sel.value : '';
    }
  }

  function gradeQuiz(subject) {
    const answers = correctAnswers[subject];
    const names = questionLabels[subject];
    let score = 0;
    let feedbackHTML = '<div class="feedback-list">';

    names.forEach((name, idx) => {
      const optDiv = document.querySelector(`#quiz-${subject} .options[data-correct]`);
      // find the specific options div for this question
      const allOptions = document.querySelectorAll(`#quiz-${subject} .options`);
      const optionDiv = allOptions[idx];
      const isMulti = optionDiv && optionDiv.getAttribute('data-type') === 'multi';
      const userAns = getAnswer(name, isMulti);
      const correctAns = answers[name] || '';

      const isCorrect = userAns.split('').sort().join('') === correctAns.split('').sort().join('') && userAns !== '';

      if (isCorrect) {
        score++;
        feedbackHTML += `<div class="result-item"><span class="correct-ans">✅ P${idx+1}:</span> Correcto</div>`;
      } else {
        const correctLetters = correctAns.toUpperCase().split('').join(', ');
        feedbackHTML += `<div class="result-item"><span class="wrong-ans">❌ P${idx+1}:</span> Tu respuesta: ${userAns ? userAns.toUpperCase() : 'Sin respuesta'} — Correcta: <strong>${correctLetters}</strong></div>`;
      }
    });
    feedbackHTML += '</div>';

    const pct = Math.round((score / 20) * 100);
    let emoji = pct >= 80 ? '🏆' : pct >= 60 ? '👍' : '📚';
    let msg = pct >= 80 ? '¡Excelente!' : pct >= 60 ? 'Buen trabajo, sigue repasando.' : 'Necesitas repasar más este tema.';

    const resultBox = document.getElementById('result-' + subject);
    resultBox.innerHTML = `
      <div class="score" style="color:${pct>=80?'#27ae60':pct>=60?'#e67e22':'#e74c3c'}">${emoji} ${score}/20</div>
      <div class="score-label">${pct}% — ${msg}</div>
      ${feedbackHTML}
    `;
    resultBox.style.display = 'block';
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

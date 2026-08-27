const fs = require('fs');
const path = require('path');

// 요일 영문 축약 매핑
const DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];

function getTodayFolderName() {
  const now = new Date();
  const yy = String(now.getFullYear()).slice(2);
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const day = DAYS[now.getDay()];
  return `${yy}${mm}${dd}_${day}`;
}

const rootDir = path.resolve(__dirname, '..');
const customFolderName = process.argv[2] || getTodayFolderName();
const targetDir = path.join(rootDir, 'daily_practice', customFolderName);

// 대상 디렉토리 생성
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// 실습 파일 수집 대상 디렉토리 목록
const sourceDirs = [
  path.join(rootDir, 'exam1', 'src'),
  path.join(rootDir, 'exam1', 'src', 'components'),
  path.join(rootDir, 'exam2', 'src', 'pages'),
  path.join(rootDir, 'exam2', 'src', 'components'),
];

console.log(`📦 [수업기록 백업] 대상 폴더: daily_practice/${customFolderName}`);
console.log('--------------------------------------------------');

let totalCopied = 0;

sourceDirs.forEach(srcDir => {
  if (!fs.existsSync(srcDir)) return;

  const files = fs.readdirSync(srcDir);
  const targetFiles = files.filter(f => {
    const stat = fs.statSync(path.join(srcDir, f));
    return stat.isFile() && (f.endsWith('.vue') || f.endsWith('.js') || f.endsWith('.ts'));
  });

  targetFiles.forEach(file => {
    // App.vue, main.js/ts, HelloWorld 등 기본 템플릿 제외 또는 포함
    const srcPath = path.join(srcDir, file);
    const destPath = path.join(targetDir, file);
    fs.copyFileSync(srcPath, destPath);
    console.log(`  ✅ 복사 완료: ${path.relative(rootDir, srcPath)} -> daily_practice/${customFolderName}/${file}`);
    totalCopied++;
  });
});

console.log('--------------------------------------------------');
console.log(`✨ 총 ${totalCopied}개의 실습 파일이 성공적으로 백업되었습니다!`);

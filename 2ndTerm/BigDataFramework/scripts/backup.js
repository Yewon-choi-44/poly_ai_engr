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
const srcDir = path.join(rootDir, 'exam1', 'src');
const customFolderName = process.argv[2] || getTodayFolderName();
const targetDir = path.join(rootDir, 'daily_practice', customFolderName);

// 대상 디렉토리 생성
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// exam1/src 직속 파일 중 .vue 파일 탐색
if (!fs.existsSync(srcDir)) {
  console.error(`❌ 소스 디렉토리를 찾을 수 없습니다: ${srcDir}`);
  process.exit(1);
}

const files = fs.readdirSync(srcDir);
const vueFiles = files.filter(f => f.endsWith('.vue'));

if (vueFiles.length === 0) {
  console.log('ℹ️  복사할 .vue 파일이 exam1/src 에 없습니다.');
  process.exit(0);
}

console.log(`📦 [수업기록 백업] 대상 폴더: daily_practice/${customFolderName}`);
console.log('--------------------------------------------------');

vueFiles.forEach(file => {
  const srcPath = path.join(srcDir, file);
  const destPath = path.join(targetDir, file);
  fs.copyFileSync(srcPath, destPath);
  console.log(`  ✅ 복사 완료: ${file} -> daily_practice/${customFolderName}/${file}`);
});

console.log('--------------------------------------------------');
console.log(`✨ 총 ${vueFiles.length}개의 .vue 파일이 성공적으로 백업되었습니다!`);

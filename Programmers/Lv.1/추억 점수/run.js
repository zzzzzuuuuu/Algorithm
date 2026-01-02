function solution(name, yearning, photo) {
  const dict = {};
  for (let i = 0; i < name.length; i++) {
    dict[name[i]] = yearning[i];
  }

  return photo.map(p =>
    p.reduce((sum, person) => sum + (dict[person] || 0), 0) // || 대신 ?? 이라고 쓰는 게 더 안전함
  );
}
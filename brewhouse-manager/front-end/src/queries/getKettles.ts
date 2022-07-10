export async function getKettles() {
  const res = await fetch('/brewhouse/kettles');
  return await res.json();
}

export async function getPumps() {
  const res = await fetch('/brewhouse/pumps');
  return await res.json();
}

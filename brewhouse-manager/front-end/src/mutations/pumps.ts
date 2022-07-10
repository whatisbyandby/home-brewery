export async function requestPumpState({
  pumpName,
  state,
}: {
  pumpName: string;
  state: boolean;
}) {
  const headers = new Headers();
  headers.append('Content-Type', 'application/json');

  const raw = JSON.stringify({
    new_state: state,
  });

  const requestOptions = {
    method: 'PUT',
    headers: headers,
    body: raw,
  };
  fetch(`/brewhouse/pumps/${pumpName}`, requestOptions);
}

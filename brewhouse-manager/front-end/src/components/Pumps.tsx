import { useQueryClient, useQuery } from 'react-query';
import { getPumps } from '../queries/getPumps';
import Pump from './Pump';

export default function Pumps() {
  const queryClient = useQueryClient();

  const { data, isError, isLoading } = useQuery('pumps', getPumps);

  if (isLoading) <h2>Loading...</h2>;
  if (isError) <h2>Error</h2>;

  console.log(data);

  return null;

  //   if (data) {
  //     return (
  //       <div>
  //         {data.map((pump) => (
  //           <Pump name={pump.stat} state={pump.state} />
  //         ))}
  //       </div>
  //     );
  //   }
}

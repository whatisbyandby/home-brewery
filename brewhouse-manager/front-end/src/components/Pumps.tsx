import { Group } from '@mantine/core';
import { useQueryClient, useQuery, useMutation } from 'react-query';
import { getPumps } from '../queries/getPumps';
import Pump, { PumpProps } from './Pump';

export default function Pumps() {
  const { data, isError, isLoading } = useQuery('pumps', getPumps);

  if (isLoading) return <h2>Loading...</h2>;
  if (isError) return <h2>Error</h2>;

  return (
    <Group>
      {data.map((pump: PumpProps) => (
        <Pump key={pump.name} name={pump.name} state={pump.state} />
      ))}
    </Group>
  );
}

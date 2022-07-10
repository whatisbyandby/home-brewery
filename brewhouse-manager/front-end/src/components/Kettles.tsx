import { Container, Group } from '@mantine/core';
import { useQueryClient, useQuery, useMutation } from 'react-query';
import { getKettles } from '../queries/getKettles';
import Kettle, { KettleProps } from './Kettle';

export default function Kettles() {
  const { data, isError, isLoading } = useQuery('kettles', getKettles);

  if (isError) return <h2>Error</h2>;
  if (isLoading) return <h2>Loading...</h2>;

  return (
    <Container>
      <Group>
        {data.map((kettle: KettleProps) => (
          <Kettle key={kettle.name} name={kettle.name} />
        ))}
      </Group>
    </Container>
  );
}

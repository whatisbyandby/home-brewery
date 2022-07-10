import { Card, Button, useMantineTheme, Center } from '@mantine/core';
import { useQueryClient, useQuery, useMutation } from 'react-query';
import { requestPumpState } from '../mutations/pumps';

export interface PumpProps {
  name: string;
  state: boolean;
}

export default function Pump(props: PumpProps) {
  const { name, state } = props;
  const theme = useMantineTheme();
  const queryClient = useQueryClient();
  const mutation = useMutation(requestPumpState, {
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries(['pumps']);
    },
  });

  const secondaryColor =
    theme.colorScheme === 'dark' ? theme.colors.dark[1] : theme.colors.gray[7];

  return (
    <div style={{ width: 340, margin: 'auto' }}>
      <Card shadow="sm" p="lg">
        <Card.Section>
          <Center>
            <h4>{name}</h4>
          </Center>
        </Card.Section>

        <Button
          variant="light"
          color={state ? 'lime' : 'grey'}
          fullWidth
          style={{ marginTop: 14 }}
          onClick={() => mutation.mutate({ pumpName: name, state: !state })}
        >
          {state ? 'Pump On' : 'Pump Off'}
        </Button>
      </Card>
    </div>
  );
}

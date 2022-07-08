import { Card, Button, useMantineTheme } from '@mantine/core';

export interface PumpProps {
  name: string;
  state: boolean;
}

export default function Pump(props: PumpProps) {
  const { name, state } = props;
  const theme = useMantineTheme();

  const secondaryColor =
    theme.colorScheme === 'dark' ? theme.colors.dark[1] : theme.colors.gray[7];

  return (
    <div style={{ width: 340, margin: 'auto' }}>
      <Card shadow="sm" p="lg">
        <Card.Section>
          <h4>{name}</h4>
        </Card.Section>

        <Button
          variant="light"
          color={state ? 'lime' : 'grey'}
          fullWidth
          style={{ marginTop: 14 }}
        >
          {state ? 'Pump On' : 'Pump Off'}
        </Button>
      </Card>
    </div>
  );
}

import { Card, Button, useMantineTheme, Center } from '@mantine/core';

export interface KettleProps {
  name: string;
}

export default function Kettle(props: KettleProps) {
  const { name } = props;
  return (
    <div>
      <Card shadow="sm" p="lg">
        <Card.Section>
          <Center>
            <h4>{name}</h4>
          </Center>
        </Card.Section>
      </Card>
    </div>
  );
}

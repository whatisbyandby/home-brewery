import { Group } from '@mantine/core';

export interface KettleProps {
  name: string;
  mode: string;
  state: string;
}

export default function Kettle(props: KettleProps) {
  const { name, mode, state } = props;
  return (
    <div>
      <Group direction="column" grow={true}>
        <h4>{name}</h4>
        <h4>{mode}</h4>
        <h4>{state}</h4>
      </Group>
    </div>
  );
}

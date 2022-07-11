import { useQueryClient, useQuery, useMutation } from 'react-query';
import { getPumps } from '../queries/getPumps';
import Pump, { PumpProps } from './Pump';

import React from 'react';
import { createStyles, Card, Group, Switch, Text } from '@mantine/core';

const useStyles = createStyles((theme) => ({
  card: {
    backgroundColor:
      theme.colorScheme === 'dark' ? theme.colors.dark[7] : theme.white,
  },

  item: {
    '& + &': {
      paddingTop: theme.spacing.sm,
      marginTop: theme.spacing.sm,
      borderTop: `1px solid ${
        theme.colorScheme === 'dark'
          ? theme.colors.dark[4]
          : theme.colors.gray[2]
      }`,
    },
  },

  switch: {
    '& *': {
      cursor: 'pointer',
    },
  },

  title: {
    lineHeight: 1,
  },
}));

interface SwitchesCardProps {
  title: string;
  description: string;
  data: {
    title: string;
    description: string;
  }[];
}

export default function SwitchesCard() {
  const { classes } = useStyles();
  const { data, isError, isLoading } = useQuery('pumps', getPumps);

  if (isLoading) return <h2>Loading...</h2>;
  if (isError) return <h2>Error</h2>;

  const items = data.map((item: any) => (
    <Group position="apart" className={classes.item} noWrap spacing="xl">
      <Text>{item.name}</Text>
      <Switch
        onLabel="ON"
        offLabel="OFF"
        className={classes.switch}
        size="lg"
      />
    </Group>
  ));

  return (
    <Card withBorder radius="md" p="xl" className={classes.card}>
      {items}
    </Card>
  );
}

import { MantineProvider, Container } from '@mantine/core';
import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
import Kettles from './components/Kettles';
import Pumps from './components/Pumps';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <MantineProvider
        theme={{ colorScheme: 'dark' }}
        withGlobalStyles
        withNormalizeCSS
      >
        <Container>
          <Kettles />
          <Pumps />
        </Container>
      </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;

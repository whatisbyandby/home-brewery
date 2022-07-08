import { MantineProvider } from '@mantine/core';
import React from 'react';
import { QueryClient, QueryClientProvider } from 'react-query';
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
        <Pumps />
      </MantineProvider>
    </QueryClientProvider>
  );
}

export default App;

import { Button, MantineProvider } from '@mantine/core';
import React from 'react';
import Pump from "./components/Pump"


function App() {
  return (
    <MantineProvider
      theme={{ colorScheme: 'dark' }}
      withGlobalStyles
      withNormalizeCSS
    >
      <div className="App">
        <Pump>This is the test button</Pump>
      </div>
    </MantineProvider>
  );
}

export default App;

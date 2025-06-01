import React from 'react';
import ReactDOM from 'react-dom/client';
import { MantineProvider } from '@mantine/core';
import { Notifications } from '@mantine/notifications';
import App from './App.tsx';
import '@mantine/core/styles.css';
import '@mantine/notifications/styles.css';
import '@/index.scss';
import { AppContextProvider } from './services/AppContext.tsx';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MantineProvider defaultColorScheme="dark">
      <Notifications />
      <AppContextProvider>
        <App />
      </AppContextProvider>
    </MantineProvider>
  </React.StrictMode>,
);

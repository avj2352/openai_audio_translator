import { type FC, type JSX, createContext, useState, type ReactNode } from 'react';
// ..custom
import AudioApi, { type IYoutubeTranscribePayload } from '@/services/AudioApi';

// create context
export const AppContext = createContext<{transcribedText: string, isLoading: boolean, fetchTranscribeText: any}>({
  transcribedText: '',
  isLoading: false,
  fetchTranscribeText: undefined
});

// create context providder

export const AppContextProvider: FC<{children: ReactNode}> = ({children}):JSX.Element => {
  // ..states
  const [transcribedText, setTranscribedText] = useState<string>('');
  const [isLoading, toggleLoading] = useState<boolean>(false);


  // api calls

  // transcribe text
  const fetchTranscribeText = async (payload: IYoutubeTranscribePayload) => {
    toggleLoading(true);  
    try {
      const response = await AudioApi.postTranscribeYoutubeUrl(payload);
      console.log('Audio API text response is: ', response);
      setTranscribedText( response?.data?.text ?? '');
    } catch(err) {
      console.log('Something went wrong: ', err);
    } finally {
      toggleLoading(false);
    }
  };

  return (
    <AppContext.Provider value = {{
      transcribedText, isLoading, fetchTranscribeText
    }}>
      {children}
    </AppContext.Provider>
  );
  
};

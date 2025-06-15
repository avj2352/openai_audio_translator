import { type FC, type JSX, createContext, useState, type ReactNode } from 'react';
import { notifications } from '@mantine/notifications';
// ..custom
import AudioApi, { type ITranslateTextPayload, type IYoutubeTranscribePayload } from '@/services/AudioApi';

type IAppContextProps = {
  transcribedText: string,
  translatedText: string,
  isLoading: boolean,
  fetchTranscribeText: any,
  fetchTranslatedText: any,
}

// create context
export const AppContext = createContext<IAppContextProps>({
  transcribedText: '',
  translatedText: '',
  isLoading: false,
  fetchTranscribeText: undefined,
  fetchTranslatedText: undefined
});

// create context providder

export const AppContextProvider: FC<{ children: ReactNode }> = ({ children }): JSX.Element => {
  // ..states
  const [transcribedText, setTranscribedText] = useState<string>('');
  const [translatedText, setTranslatedText] = useState<string>('');
  const [isLoading, toggleLoading] = useState<boolean>(false);


  // ..show notifications
  const showNotification = (msg: string, color: 'green' | 'red') => {
    notifications.show({
      title: 'Notification!',
      message: msg,
      color: color,
    })
  }



  // api calls

  // transcribe text
  const fetchTranscribeText = async (payload: IYoutubeTranscribePayload) => {
    toggleLoading(true);
    try {
      const response = await AudioApi.postTranscribeYoutubeUrl(payload);
      // console.log('Audio API text response is: ', response);
      showNotification('Video transcribe successful', 'green');
      setTranscribedText(response?.data?.text ?? '');
    } catch (err) {
      console.log('->> (transcribe) Something went wrong: ', err);
      showNotification('Video transcribe failed!', 'red');
    } finally {
      toggleLoading(false);
    }
  };


  // translate text
  const fetchTranslatedText = async (payload: ITranslateTextPayload) => {
    toggleLoading(true);
    try {
      const response = await AudioApi.postTranslateText(payload);
      console.log('Audio API translate text response is: ', response);
      showNotification(`Text translation to ${payload.to_language} successful`, 'green');
      setTranslatedText(response?.data?.text ?? '');
    } catch (err) {
      console.log('->> (translate) Something went wrong: ', err);
      showNotification('Text translation failed!', 'red');
    } finally {
      toggleLoading(false);
    }
  }; 

  return (
    <AppContext.Provider value={{
      transcribedText, translatedText,
      isLoading, fetchTranscribeText,
      fetchTranslatedText,
    }}>
      {children}
    </AppContext.Provider>
  );

};

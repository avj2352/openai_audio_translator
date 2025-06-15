import { AudioApiInstance } from "@/services/AudioApiInstance";

export type IYoutubeTranscribePayload = {
  url: string;
  filename: string;
};

export type ITranslateTextPayload = {
  content: string;
  from_language: "english";
  to_language: "hindi" | "tamil";
};

const AudioApi = {
  postTranscribeYoutubeUrl: (
    payload: IYoutubeTranscribePayload
  ): Promise<any> => {
    console.log("translate youtube post data payload is: ", payload);
    return AudioApiInstance.post(`/transcribe/youtube`, payload);
  },
  postTranslateText: (payload: ITranslateTextPayload): Promise<any> => {
    console.log("translate selected text to: ", payload.to_language);
    return AudioApiInstance.post(`/prompt/translate`, payload);
  },
};

export default AudioApi;

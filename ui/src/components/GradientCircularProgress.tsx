/**
* Gradient circular spinner loader
*/
import { Fragment, type FC, type JSX } from 'react';
import { Loader } from '@mantine/core';


type IGradientCircularProgressProps = {
  isLoading: boolean;
}


const GradientCircularProgress: FC<IGradientCircularProgressProps> = ({ isLoading }): JSX.Element => {
  return isLoading ? <Loader color="blue" type="dots" style={{
    margin: 5,
    marginTop: 10
  }} /> : <Fragment/>;
};

export default GradientCircularProgress;

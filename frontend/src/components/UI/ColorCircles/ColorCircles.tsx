import ColorCircle from '../ColorCircle/ColorCircle';
import styles from './ColorCircles.module.scss';
import { ColorCirclesPropsType } from './ColorCirclesTypes';

const ColorCircles = ({moveIndicator}: ColorCirclesPropsType) => {
  return (
    <div className={styles.container}>
      <ColorCircle color='blue' position='left' moveIndicator={moveIndicator}/>
      <ColorCircle color='yellow' position='right' moveIndicator={moveIndicator}/>
    </div>
  );
};

export default ColorCircles;
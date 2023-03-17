import cn from 'classnames';
import { useEffect, useRef } from 'react';
import styles from './ColorCircle.module.scss';
import { ColorCirclePropsType } from './ColorCircleTypes';

const k = 5

const ColorCircle = ({position, color, moveIndicator}: ColorCirclePropsType) => {
  const ref = useRef<HTMLElement>(null)

  useEffect(() => {
    if (!ref.current) {
      return
    }
   
    const el = ref.current
    if (position === 'right') {
      el.style.top = 17.5 - moveIndicator.y / window.innerHeight * k + '%'
      el.style.right = (-4000 - moveIndicator.x) / window.innerWidth * k + '%'
    } else {
      el.style.bottom = 17.5 - moveIndicator.y / window.innerHeight * k + '%'
      el.style.left = (-4000 - moveIndicator.x) / window.innerWidth * k + '%'
    }

  }, [moveIndicator])


  return (
    <span
      ref={ref}
      className={cn(styles.circle, styles[color], styles[position])
    }></span>
  );
};

export default ColorCircle;
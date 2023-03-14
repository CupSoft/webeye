import cn from 'classnames';
import { useEffect, useRef } from 'react';
import styles from './ColorCircle.module.scss';
import { ColorCirclePropsType } from './ColorCircleTypes';

const ColorCircle = ({position, color, moveIndicator}: ColorCirclePropsType) => {
  const ref = useRef<HTMLElement>(null)

  useEffect(() => {
    if (!ref.current) {
      return
    }
    const el = ref.current
    
    if (position === 'right') {
      el.style.top = el.offsetTop - moveIndicator.y / window.innerHeight * 100 + 'px'
      el.style.left = el.offsetLeft - moveIndicator.x / window.innerWidth * 100 + 'px'
    } else {
      el.style.top = el.offsetTop + moveIndicator.y / window.innerHeight * 100 + 'px'
      el.style.left = el.offsetLeft + moveIndicator.x / window.innerWidth * 100 + 'px'
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
import React from 'react';
import styles from './Input.module.scss'
import { InputPropsType } from './InputTypes';

const Input = ({name, options, register, ...props}: InputPropsType) => {
  return (
    <input
      {...props}
      {...register(name as string, options)}
      className={styles.input}
    />
  );
};

export default Input;
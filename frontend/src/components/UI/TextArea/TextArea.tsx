import React from 'react';
import styles from './TextArea.module.scss'
import { TextAreaPropsType } from './TextAreaTypes';

const TextArea = (props: TextAreaPropsType) => {
  return (
    <textarea className={styles.textarea} {...props}></textarea>
  );
};

export default TextArea;
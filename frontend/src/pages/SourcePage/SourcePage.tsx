import React from 'react';
import { useParams } from 'react-router-dom';
import styles from './SourcePage.module.css'

const SourcePage = () => {
  const params = useParams()
  return (
    <div>
      {`Source: ${params.id}`}
    </div>
  );
};

export default SourcePage;
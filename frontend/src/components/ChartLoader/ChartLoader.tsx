import React from 'react';
import ContentLoader from 'react-content-loader';

const ChartLoader = () => {
  return (
    <ContentLoader 
      speed={2}
      width='93%'
      height='49vh'
      backgroundColor="#1c253d"
      foregroundColor="#2f364e"
      style={{
        border: '1px solid rgb(40, 45, 69)',
        maxWidth: '105rem',
        minHeight: '15rem',
        marginTop: '.5rem',
        borderRadius: '.5rem'
      }}
    >
      <rect 
        width="210%" 
        height="100%" 
      /> 
    </ContentLoader>
  );
};

export default ChartLoader;
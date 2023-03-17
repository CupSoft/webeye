import { useState } from 'react';
import Card from '../Card/Card';
import ReportsList from './ReportsList/ReportsList';
import styles from './SocialNetworksCard.module.scss';
import { SocialNetworksCardPropsType } from './SocialNetworksCardTypes';
import SocialReportsList from './SocialReportsList/SocialReportsList';

const SocialNetworksCard = ({sourceUuid, sourceName, ...props}: SocialNetworksCardPropsType) => {
  const [sourceSelect, setSourceSelect] = useState('webeye')

  function sourceSelectChangeHandler(evt: React.ChangeEvent<HTMLSelectElement>) {
    setSourceSelect(evt.target.value)
  }

  return (
    <Card 
      title='Что пишут люди об этом ресурсе?'
      description='Просматривайте актуальные сообщения от пользователей'
      {...props}
      scrolled={false}
    >
      <>
        <select 
          name="source_select" 
          id="source_select"
          value={sourceSelect}
          onChange={sourceSelectChangeHandler}
          className={styles.source_select}
        >
          <option value="socials">
            В социальных сетях
          </option>
          <option value="webeye">
            На сайте
          </option>
        </select>
        {
          sourceSelect === 'socials' 
          ? <SocialReportsList sourceUuid={sourceUuid}/>
          : <ReportsList 
              sourceUuid={sourceUuid}
              sourceName={sourceName}
            />}
        {/* <hr className={styles.hr}/> */}
      </>
    </Card>
  );
};

export default SocialNetworksCard;
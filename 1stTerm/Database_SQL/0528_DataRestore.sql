insert into ctrl_unitreportloh set note='미등록';
select * from ctrl_unitreportloh where note='미등록';
create index note_ix on ctrl_unitreportlog(note);
select * from ctrl_unitreportlog where note='미등록';

create index  note_ix on ctrl_unitreportlog(note);
select * from ctrl_unitreportlog;
#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��4�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE ��i v2.1
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE v0.21
#�@programed by CUMRO
#�@http://cgi.members.interq.or.jp/sun/cumro/mm/
#�@cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(��) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi�@		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;
#-----------------------------------------------------------------------------#

if($mente) { &error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B"); }

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

&rank;
exit;

#------------------#
#  �����L���O�\��  #
#------------------#
sub rank {

	if (!$no_html) { &error("���ׂ��傫���̂�HTML�����ł��Ȃ��T�[�o�[�ł͎g�p�ł��܂���"); }

	$lock_file = "$lockfolder/tim.lock";
	&lock($lock_file,'TM');
	open(IN,"$all_data_time");
	@all_time = <IN>;
	close(IN);

	$hit=0;
	foreach(@all_time){
		($rankmode,$ranktime) = split(/<>/);
		if ($rankmode eq "sranking") { $hit=1;last; }
	}

	$lrtime = time();
	$btime = $lrtime - $ranktime;
	$ztime = int($btime/3600);
	$ranking_make = 0;

	if ($btime > 3600*24 || !$hit) {

		$hit=0;
		@item_new=();
		foreach (@all_time) {
			($rankmode,$ranktime) = split(/<>/);
			if ($rankmode eq "sranking") {
				unshift(@item_new,"sranking<>$lrtime<>\n");
				$hit=1;
			} else {
				push(@item_new,"$_");
			}
		}

		if (!$hit) { unshift(@item_new,"sranking<>$lrtime<>\n"); }

		open(OUT,">$all_data_time");
		print OUT @item_new;
		close(OUT);
		$lock_file = "$lockfolder/tim.lock";
		&unlock($lock_file,'TM');

		$ranking_make = 1;

	} else {
		$lock_file = "$lockfolder/tim.lock";
		&unlock($lock_file,'TM');
	}

	if ($ranking_make) {

	&all_data_read;

	$sousu = @RANKING;

	# �z��19�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[18]} @RANKING;
	@levela = @RANKING[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��17�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[16]} @levela;
	@hitp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��8�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[7]} @levela;
	@atack = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��9�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[8]} @levela;
	@def = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��10�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[9]} @levela;
	@rp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��11�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[10]} @levela;
	@gp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��12�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[11]} @levela;
	@sp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��13�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[12]} @levela;
	@bp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��14�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[13]} @levela;
	@lp = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	# �z��21�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[20]} @levela;
	@yen = @levela[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	foreach(@levela){
		@chara = split(/<>/);

		if ($chara[21] > 1000) {
			$kati_ritu = int($chara[22]*10000/$chara[21])/100;
			unshift(@win_new,"$chara[4]<>$chara[3]<>$chara[2]<>$kati_ritu<>$chara[21]<>$chara[18]<>$chara[0]<>\n");
		}
	}

	# �z��3�ԖڂŃ\�[�g
	@tmp = map {(split /<>/)[3]} @win_new;
	@win_new = @win_new[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];


	$buffer = <<"EOM";
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="Pragma" content="no-cache">
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="Content-Script-Type" content="text/javascript">
<META http-equiv="Content-Style-Type" content="text/css">
<SCRIPT Language="JavaScript" src="$java_script" type="text/javascript">
</SCRIPT>
<STYLE type="text/css">
<!--
BODY{
  font-family : $font_name;
  font-size:12px;
  color:$text;
  background-image : url($html_path$backgif);
  background-attachment : fixed;
}
.red{font-family : $font_name;color:$red;}
.yellow{font-family : $font_name;color:$yellow;}
.blue{font-family : $font_name;color:$blue;}
.green{font-family : $font_name;color:$green;}
.white{font-family : $font_name;color:$white;}
.dark{font-family : $font_name;color:$dark;}
.small{font-size:8px;$font_name;color:$red;}
//-->
</STYLE>
<link rel="stylesheet" href="$html_path$style_sheet" type="text/css">
<title>$main_title</title></head>
<body background="$html_path$backgif" bgcolor="$bgcolor" text="$text" link="$link" vlink="$vlink" alink="$alink">
EOM
		if ($midi_set) {
			$buffer .= "<embed src=\"$html_path$midi\" type=\"audio/midi\" height=\"2\" autostart=\"true\" repeat=\"true\" save=\"false\" volume=\"100\" width=\"2\">\n";
		}
	local(@mody)=localtime($ltime);
	$mody[4]++;

		$buffer .= <<"EOM";
<H3>�p�Y�����̋L�^</H3>
<FONT SIZE="3">���ꂼ��̃X�e�[�^�X��TOP10��\\�����Ă��܂��B<br>
<font size =3 color =red><b>�������A�X�V�͂P���ɂP�񂵂��s���܂���B</b></font>�O���$mody[4]��$mody[3]��$mody[2]��$mody[1]���ɍX�V����܂����B<br>

�S�o�^�L�����N�^�[���́A<B>$sousu</B>�l�ł��B
</FONT>
<HR SIZE=0>
EOM
	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="���x��</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">LV</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@levela){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[18]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}

	$buffer.="</TABLE>\n";

	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="HP</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">HP</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@hitp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[16]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";

	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="������</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">������</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@atack){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[7]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";

	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="�m\�\\</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">�m\�\\</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@def){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[8]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";


	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="�M�S</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">�M�S</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@rp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[9]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";



	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="������</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">������</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@gp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[10]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";



	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="��p��</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">��p��</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@sp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[11]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";



	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="����</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">����</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@bp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[12]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";



	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="����</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">����</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@lp){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[13]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";

	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="�J���}</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">�J���}</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@yen){
		@chara = split(/<>/);
		$url="<A HREF=\"$chara[3]\" TARGET=\"_blank\">$chara[2]</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="$chara[20]\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";

	$buffer.="<TABLE BORDER=0>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b2\" COLSPAN=\"5\">\n";
	$buffer.="����</TD></TR>\n";
	$buffer.="<TR><TD ALIGN=\"center\" CLASS=\"b1\"></TD><TD ALIGN=\"center\" CLASS=\"b1\">�Ȃ܂�</TD><TD ALIGN=\"center\" CLASS=\"b1\">����</TD><TD ALIGN=\"center\" CLASS=\"b1\">�z�[���y�[�W</TD>\n";

	$i=1;
	foreach(@win_new){
		($kname,$kurl,$ksite,$kati_ritu,$ktotal,$klv,$kid)=split(/<>/);
		$url="<A HREF=\"http\:\/\/$kurl\" TARGET=\"_blank\">$ksite</A>";
		$buffer.="<TR><TD ALIGN=\"right\">\n";
		$buffer.="<B>$i</B></TD>\n";
		$buffer.="<TD>\n";
		$buffer.="<a href=\"../$scripta?mode=chara_sts&id=$kid\">$kname</a>\n";
		$buffer.="</TD>\n";
		$buffer.="<TD ALIGN=\"right\">\n";
		$buffer.="<b>$kati_ritu</b>��($ktotal��)\n";
		$buffer.="</TD>\n";
		$buffer.="<TD>\n";
		$buffer.="$url\n";
		$buffer.="</TD>\n";
		$buffer.="</TR>\n";
		$i++;
		if($i >10){last;}
	}
	$buffer.="</TABLE>\n";

	$buffer.= <<"EOM";
<HR SIZE=0 WIDTH="100%">
<a href = "$html_path$scripto">$main_title��TOP��</a>
<HR SIZE=0 WIDTH="100%"><DIV align=right>
FFA ������ver2.00 edit by <a href="http://www.eriicu.com" target="_top">����</a><br>
FFA Emilia Ver1.01 remodeled by Classic(��)<br>
FF Battle De I v3.06 remodeling by <a href="http://www.mj-world.jp/" target="_blank">jun-k</a>(�X�V��~��)<br>
FF ADVENTURE(��) v1.040 remodeled by <a href="http://www.gun-online.com" target="_blank">�f�t�m</a><br>
FF ADVENTURE v0.43 edit by D.Takamiya(CUMRO) <a href="http://www5c.biglobe.ne.jp/~ma-ti/" target="_blank">���z�z��(�Ǘ���ma-ti)</a><br>
</DIV></body></html>
EOM

		open(LOG,">./rankhtml/sougorank.html");
		print LOG $buffer;
		close(LOG);

	}

        print "Location: $no_html/sougorank.html\n\n";

	exit;

}

#!/usr/local/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��3�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
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
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#     http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi 		#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �퓬���C�u�����̓ǂݍ���
require 'battle.pl';
# �`�����v��p���C�u�����ǂݍ���
require 'wbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $battle_back;
$midi = $battle_midi;


#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if ($mode) { &$mode; }

&log_in;

exit;

#------------#
#  ��t���  #
#------------#
sub log_in{

	&chara_load;

	&chara_check;

	&header;

	print << "EOM";
<h1>�D���ȃL�����ɒ���</h1>
<hr size=0>
<FONT SIZE=3>
<B>�ē��l</B><BR>
�u
�悤������������Ⴂ�܂����I<br>
�����ł͂���$main_title�̍D���ȃv���C���[�ɘr������������邱�Ƃ��ł��܂��I<br>
�������A�o���l�E�����͓���ł��܂���B�����܂ł��r���������ł��B<br>
���Ȃ���$chara[4]����ł��ˁI���킵�Ă݂܂����H
�v
<form action="$script_select" method="post">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
���O�w��
<input type="text" name="aitename" value="" size="20"><br>
<input type="submit" class="btn" value="���킷��">
</form>
<form action="$script_select" method="post">
<input type="hidden" name="mode" value="sentaku">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="���O���ꗗ����I������">
</form>
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;

}

#------------#
#  �I�����  #
#------------#
sub sentaku{

	&chara_load;

	&chara_check;

	&all_data_read;

	&header;

	print << "EOM";
<h1>�ꗗ����I��</h1>
<hr size=0>
<FONT SIZE=3>
<B>�ē��l</B><BR>
�u
�ǂ̕��Ɛ���܂����H
�v
<form action="$script_select" method="post">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<table width = "80%"><tr>
EOM
	foreach (@RANKING) {
		s/\n//gi;
		s/\r//gi;
		@aite_data = split(/<>/);
		print << "EOM";
<td align="left" class="b2" width = "20%">
<input type = "radio" name = "aiteid" value = "$aite_data[0]">
$aite_data[4](Lv.$aite_data[18])
</td>
EOM
		$a++;
		if ($a % 5 == 0) {
			print "</tr><tr>";
		}
	}
	print << "EOM";
</tr></table>
<input type="submit" class="btn" value="���킷��">
</form>
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;

}

#------------#
#  �퓬���  #
#------------#
sub battle {

	&get_host;

	&chara_load;

	&chara_check;

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;

	if ($vtime > 0) {
		if ($ltime < $b_time) {
			&error("����$vtime�b�ԓ����܂���B");
		}
	}

	if (!$in{'aiteid'}) {
		$form = << "EOM";
<form action="$script_select" method="post">
<input type="hidden" name="mode" value="battle">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
������x���O�w��
<input type="text" name="aitename" value="" size="20"><br>
<input type="submit" class="btn" value="���킷��">
</form>
EOM
		&all_name_search($in{'aitename'},$form);
	} else {
		$aiteid = $in{'aiteid'};
	}

	open(IN,"./charalog/$aiteid.cgi");
	$aite_data = <IN>;
	close(IN);

	@winner_data = split(/<>/,$aite_data);

	&winner_data;

	# �܋��̌���
	$gold = 0;

	&item_load;

	&acs_add;

	&wacs_add;

	$khp_flg = $chara[15];
	$whp_flg = $winner[15];

	$i=1;$j=0;@battle_date=();
	foreach (1..$turn) {

		&shokika;

		&tyousensya;
		&winner_atack;

		&tyosenwaza;
		&winwaza;

		&acs_waza;
		&wacs_waza;

		&battle_clt;
		&battle_kaihi;

		&battle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	&header;

	print "<h1>$chara[4]�́A$winner[3]�ɐ킢�𒧂񂾁I�I</h1>\n<hr size=0><br>\n";

	$i=0;
	foreach(@battle_date){
		print "$battle_date[$i]";
		$i++;
	}
	
	if ($win) {
		print "$comment<br>\n";
	} else {
		print "$comment<br>\n";
	}

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

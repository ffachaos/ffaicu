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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B     	#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B   	#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="$acs_shop" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  �A�C�e���\��  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"$acs_file");
	@log_acs = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_acs){
		($a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_6up,$a_lpup,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($chara[31] eq "$a_no"){ $hit=1;last; }
	}

	if(!$hit) {
		$a_name="�Ȃ�";
		$a_gold="0";
		$a_ex = "-";
	}

	$ui_gold = int($a_gold / 3) * 2;


	open(IN,"$acs_folder/acs$chara[14].ini");
	@acs_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>�A�N�Z�T���[�V���b�v</h1>
<hr size=0>

<FONT SIZE=3>
<B>�����i���̃}�X�^�[</B><BR>
�u�ӂ��B�B��₩���Ȃ炳�����ƋA��ȁB�B�B<BR>
�@��H�A���܂�<B>$chara[4]</B>����Ȃ����B
<BR>���܂����ɂ��Ȃ�$chara_syoku[$chara[14]]������Ă�炵������Ȃ����B�B�B
<BR>
���̓X�̕i�������܂����Ƃ����g�����Ȃ���Ǝv���Ă���̂��H
<BR><BR>�ŁA�ǂ�𔃂��񂾁H�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>����</th><th>���i</th></tr>
<tr>
<form action="$acs_shop" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̑����i</th><th>$a_name</th><th>$a_ex</th><th>$ui_gold</th></tr></table>
<form action="$acs_shop" method="post">
<table>
<tr>
<th></th><th>No.</th><th>�Ȃ܂�</th><th>����</th><th>���i</th></tr>
EOM

	foreach (@acs_array) {
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_6up,$ai_lpup,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $ai_gold) {
			print "<input type=radio name=item_no value=\"$ai_no\">";
		} else {
			print "�~";
		}
		print "</td><td align=right class=b1>$ai_no</td><td class=b1>$ai_name</td><td align=right class=b1>$ai_msg</td><td align=right class=b1>$ai_gold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�����i�𔃂�">
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$acs_folder/acs$chara[14].ini");
	@acs_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_6up,$ai_lpup,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($in{'item_no'} eq "$ai_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[19] < $ai_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ai_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("�����i�q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_6up<>$ai_lpup<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);
	&unlock($lock_file,'SA');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�����i���̃}�X�^�[</B><BR>
�u���x����`�I<br>
�����������i�͂��񂽂̑����i�q�ɂɑ����Ă�������I
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_sell {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$acs_file");
	@acs_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@acs_array){
		($i_no,$i_name,$i_gold) = split(/<>/);
		if($chara[31] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if(!$chara[31]) { &error("����ȃA�C�e���͑��݂��܂���"); }
	$ui_gold = int($i_gold / 3) * 2;

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[31] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&acs_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

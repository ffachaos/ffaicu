#------------------#
#�@���b�Z�[�W�\���@#
#------------------#
	print "�y���M�������b�Z�[�W�z�\\����<b>$max_gyo</b>���܂�";
	open(IN,"$sousin_file/$chara[0].cgi");
	@MESSAGE_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@MESSAGE_LOG){
		($hid,$hname,$htime,$hmessage,$hhost) = split(/<>/);
		if ($max_gyo < $i) {
			last;
		}
		print <<"EOM";
<hr size=0>
<table><tr>
<td>
<font color="$red">
<small><b>$hname�����</b>�@�� �u<b>$hmessage</b>�v$htime\[$hhost\]</small>
</font>
</td>
EOM

		print <<"EOM";
</tr></table>
EOM
		$hit=1;$i++;
	}
	if(!$hit){
		print "<hr size=0><font color=$red>$chara[4]���񂪑��M�������b�Z�[�W�͂���܂���</font>\n";
	}
	print "<hr size=0>";

1;
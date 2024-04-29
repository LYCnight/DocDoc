#include <vector>
#include <queue>
#include <ctime>
#include <iostream>
using namespace std;

struct Heading{
    int id;
    int level;
    vector<int> dep;
    string heading;
    string text;
    vector<string> dep_text; // 暂时还没用上
    Heading(int id, string heading, vector<int> dep, int level){
        this->id = id;
        this->heading = heading;
        this->dep = dep;
        this->level = level;
    }
};

class TreeNode{
public:
    Heading *heading;
    vector<TreeNode*> childlist;
    TreeNode(Heading *heading){
        this->heading = heading;
    }
};

void buildTree(vector<Heading*> content, int &i, TreeNode* cur){
    // 归来
    if(i >= content.size())
        return;
    
    // 不能纳为孩子，则向上返回
    if(content[i]->level <= cur->heading->level)
        return;
    // 可以纳为孩子，则继续向深层递归
    while(i < content.size() && content[i]->level > cur->heading->level){
        TreeNode *childNode = new TreeNode(content[i]);
        cur->childlist.push_back(childNode);
        i += 1;
        buildTree(content, i, childNode);
    }
    // 所有的孩子都纳入完毕，向上回溯
    return;
}

vector<vector<string>> order(TreeNode* root){
    vector<vector<string>> result;
    queue<TreeNode*> que;
	if(root != nullptr)
    	que.push(root);
    while(que.empty() != true){
        int size = que.size();
        vector<string> vec;
        for(int i = 0; i < size; i++){
            TreeNode* cur = que.front();
            que.pop();
            vec.push_back(cur->heading->heading);
            for(TreeNode* node : cur->childlist){
                que.push(node);
            }
        }
        result.push_back(vec);
    }
    return result;
}

void printTree(TreeNode *root){
    vector<vector<string>> result = order(root);
	for(vector<string> vec : result){
		cout << "[";
		for(int j = 0; j < vec.size()-1; j++)
			cout << vec[j] << ",";
		cout << vec[vec.size()-1] << "]";
	}
}

bool mutation(double mutation_prob){
    // 生成一个介于0到1之间的随机概率
    double pro = (double)rand() / RAND_MAX;
    if(pro <= mutation_prob)
        return true;
    else
        return false;
}

string write_without_dep(string title, string heading, vector<int> dep){
    cout << "write_without_dep:"  << endl;
    cout << "title: <" << title << ">"  << endl;
    cout << "heading: " << heading << endl;
    cout << "depText: ";
    cout << "[";
    for(int i = 0 ; i < dep.size()-1; i++){
        cout << dep[i] << ",";
    }
    cout << dep[dep.size() - 1] << "]" << endl;
    cout << endl;

    string newText = "这是" + heading + "的文本";
    return newText;
}

string write_with_dep(string title, string heading, vector<int> dep, vector<string> dep_text){
    cout << "write_with_dep:"  << endl;
    cout << "title: <" << title << ">"  << endl;
    cout << "heading: " << heading << endl;
    cout << "dep: ";
    cout << "[";
    for(int i = 0 ; i < dep.size()-1; i++){
        cout << dep[i] << ",";
    }
    cout << dep[dep.size() - 1] << "]" << endl;
    cout << "dep_text:";
    cout << "[";
    for(int i = 0 ; i < dep_text.size()-1; i++){
        cout << dep_text[i] << ",";
    }
    cout << dep_text[dep_text.size() - 1] << "]" << endl;
    cout << endl;

    string dep_text_str;
    for(int i = 0 ; i < dep_text.size()-1; i++){
        dep_text_str += dep_text[i] + ",";
    }
    dep_text_str += dep_text[dep_text.size()-1];

    string newText = "这是`" + heading + "`的内容， 依赖于[" + dep_text_str + "]";
    return newText; 
}

string write_mutation(string title, string heading, vector<int> dep, vector<string> dep_text){
    cout << "write_mutation:"  << endl;
    cout << "title: <" << title << ">"  << endl;
    cout << "heading: " << heading << endl;
    cout << "depText: ";
    cout << "[";
    for(int i = 0 ; i < dep.size()-1; i++){
        cout << dep[i] << ",";
    }
    cout << dep[dep.size() - 1] << "]" << endl;
    cout << endl;

    string dep_text_str;
    for(int i = 0 ; i < dep_text.size()-1; i++){
        dep_text_str += dep_text[i] + ",";
    }
    dep_text_str += dep_text[dep_text.size()-1];

    string newText = "这是`" + heading + "`的内容， 总结于：[" + dep_text_str + "]";
    return newText; 
}

vector<string> getDeptext(vector<Heading*> content ,vector<int> dep){
    vector<string> dep_text;
    for(int dep_id : dep){
        dep_text.push_back(content[dep_id]->text);
    }
    return dep_text;
}

bool isGenPost(vector<int> dep, int id){
    if(dep == vector<int>{-1})
        return false;
    for(int i : dep){
        if(id >= i){
            return false;
        }
    }
    return true;
}

void genDocPre(TreeNode* cur, string title, double mutation_prob, vector<Heading*> content){
    string heading = cur->heading->heading;
    vector<int> dep = cur->heading->dep; 
    // 归来（如果是叶子节点，则归来）
    if(cur->childlist.empty() == true){
        if(dep == vector<int>{-1}){
            string newText = write_without_dep(title, heading, dep);
            cur->heading->text = newText;
        }
        else{
            if(isGenPost(cur->heading->dep, cur->heading->id) == true)
                return;
            vector<string> dep_text = getDeptext(content, dep);
            string newText =  write_with_dep(title, heading, dep, dep_text);
            cur->heading->text = newText;  // 更新节点内容
            cur->heading->dep_text = dep_text; // 更新当前节点的 dep_text
            //cur->heading->dep = vector<int>{-1}; // 将节点依赖更新为 {-1}
        }
        return;
    }
    // 子递出
    for(TreeNode* childNode : cur->childlist){
        genDocPre(childNode, title, mutation_prob, content);
    }
    // 回溯
    return;
}


void genDocPost(string title, TreeNode* cur, vector<Heading*> content){
    // 中处理
    if(cur->childlist.empty() == true){ // 如果是叶子节点
        if(isGenPost(cur->heading->dep, cur->heading->id) == true){
            vector<string> dep_text = getDeptext(content, cur->heading->dep);
            string newText = write_with_dep(title, cur->heading->heading, cur->heading->dep, dep_text);
            cur->heading->dep_text = dep_text; // 更新当前节点的 dep_text 
            cur->heading->text = newText;
        }
        return;
    }
    // 子递出
    for(int i = cur->childlist.size()-1 ; i >= 0 ; i--){
        genDocPost(title, cur->childlist[i], content);
    }
    // 回溯
    return;
}


void genDocMutation(TreeNode* cur, string title, double mutation_prob, vector<Heading*> content){
    string heading = cur->heading->heading;
    vector<int> dep = cur->heading->dep; 
    // 归来（为叶子节点，则归来）
    if(cur->childlist.empty() == true){
        return;
    }
    // 子递出
    for(TreeNode* childNode : cur->childlist){
        genDocMutation(childNode, title, mutation_prob, content);
    }
    // 回溯，处理突变节点
    if(cur->heading->level > 0 && mutation(mutation_prob) == true){
        // 获取下一层子节点的heading
        dep.clear(); // 发生突变，则清空当前节点的依赖
        // 获取下一层所有子节点的id，作为当前节点的依赖
        for(TreeNode *node : cur->childlist){
            dep.push_back(node->heading->id);
        }
        vector<string> dep_text = getDeptext(content, dep);
        string newText = write_mutation(title, heading, dep, dep_text);
        // 更新依赖
        cur->heading->dep = dep;
        cur->heading->dep_text = dep_text;
        cur->heading->text = newText;
    }
    // 回溯
    return;
}

string strRepeat(string str, int repeat){
    if(repeat < 1){
		throw runtime_error("错误，repeat必须大于等于1");
    }
	string newStr;
    for(int i = 0; i < repeat; i++){
        newStr += str;
    }
    return newStr;
}

string DocAssemble(vector<Heading*> content){
    string fulltext;
    Heading* title = content[0];
    fulltext += title->heading + "\n";
    for(Heading* heading : content){
        if(heading->level > 0){
            cout << "heading: " << heading->heading << ", heading->level = " << heading->level << endl;
            fulltext += strRepeat("#", heading->level) + " " + heading->heading + "\n";
            fulltext += heading->text + "\n";
        }
    }
    return fulltext;
}

int main(){
    srand(time(nullptr)); // 设置随机种子

	vector<Heading*> content;
    content.push_back(new Heading(0, "root", {-1}, 0));
    content.push_back(new Heading(1, "A", {-1}, 1));
    content.push_back(new Heading(2, "B", {-1}, 2));
    content.push_back(new Heading(3, "C", {-1}, 3));
    content.push_back(new Heading(4, "D", {3}, 3));
    content.push_back(new Heading(5, "E", {4}, 3));
    content.push_back(new Heading(6, "F", {12}, 2));
    content.push_back(new Heading(7, "G", {-1}, 1));
    content.push_back(new Heading(8, "H", {-1}, 2));
    content.push_back(new Heading(9, "L", {-1}, 3));
    content.push_back(new Heading(10, "I", {-1}, 2));
    content.push_back(new Heading(11, "J", {3}, 3));
    content.push_back(new Heading(12, "K", {-1}, 3));

    // 打印节点文本    
    for(Heading* heading : content){
        cout << heading->heading << "'s text: `" << heading->text << endl;
    }

    // for(Heading* heading : content){
    //     heading->text = "这是`" + heading->heading + "`的文本";
    // }

	// 打印节点依赖
	// for(Heading* heading : content){
    //     cout << heading->heading << ", ";
	// 	cout << "[";
	// 	for(int dep_id : heading->dep){
	// 		cout << dep_id << ",";
	// 	}
	// 	cout << "]" << endl;
    // }

    TreeNode *root = new TreeNode(content[0]);
    // cout << root->heading->heading << endl;
	
	int i = 1;
	buildTree(content, i, root);    // 构建N叉树
    printTree(root);    // 层序遍历打印

    string title = "DocDoc";
	double mutation_prob = 1; // 突变概率
    genDocPre(root, title, mutation_prob, content);    // 生成文本（反向依赖生成）
    
    // // 打印节点文本    
    // for(Heading* heading : content){
    //     cout << heading->heading << "'s text: `" << heading->text << endl;
    // }

    genDocPost(title, root, content);     // 生成文本（正向依赖生成）

    // // 打印节点文本    
    // for(Heading* heading : content){
    //     cout << heading->heading << "'s text: `" << heading->text << endl;
    // }

    genDocMutation(root, title, mutation_prob, content);    // 生成文本（突变节点）
    // // 打印节点文本    
    // for(Heading* heading : content){
    //     cout << heading->heading << "'s text: `" << heading->text << endl;
    // }

    string fulltext = DocAssemble(content);

    cout << fulltext;

	// // 打印节点依赖
	// for(Heading* heading : content){
    //     cout << heading->heading << ", ";
	// 	cout << "[";
	// 	for(int dep_id : heading->dep){
	// 		cout << dep_id << ",";
	// 	}
	// 	cout << "]" << endl;
    // }
}







